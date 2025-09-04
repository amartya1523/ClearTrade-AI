"use client"

import { useEffect, useRef, useState } from "react"
import { cn } from "@/lib/utils"
import { Button } from "@/components/ui/button"

class TextScramble {
  el: HTMLElement
  chars: string
  queue: Array<{ from: string; to: string; start: number; end: number; char?: string }>
  frame: number
  frameRequest: number
  resolve: (value: void | PromiseLike<void>) => void

  constructor(el: HTMLElement) {
    this.el = el
    this.chars = "!<>-_\\/[]{}—=+*^?#"
    this.queue = []
    this.frame = 0
    this.frameRequest = 0
    this.resolve = () => {}
    this.update = this.update.bind(this)
  }

  setText(newText: string) {
    const oldText = this.el.innerText
    const length = Math.max(oldText.length, newText.length)
    const promise = new Promise<void>((resolve) => (this.resolve = resolve))
    this.queue = []

    for (let i = 0; i < length; i++) {
      const from = oldText[i] || ""
      const to = newText[i] || ""
      const start = Math.floor(Math.random() * 40)
      const end = start + Math.floor(Math.random() * 40)
      this.queue.push({ from, to, start, end })
    }

    cancelAnimationFrame(this.frameRequest)
    this.frame = 0
    this.update()
    return promise
  }

  update() {
    let output = ""
    let complete = 0

    for (let i = 0, n = this.queue.length; i < n; i++) {
      let { from, to, start, end, char } = this.queue[i]
      if (this.frame >= end) {
        complete++
        output += to
      } else if (this.frame >= start) {
        if (!char || Math.random() < 0.28) {
          char = this.chars[Math.floor(Math.random() * this.chars.length)]
          this.queue[i].char = char
        }
        output += `<span class="dud">${char}</span>`
      } else {
        output += from
      }
    }

    this.el.innerHTML = output
    if (complete === this.queue.length) {
      this.resolve()
    } else {
      this.frameRequest = requestAnimationFrame(this.update)
      this.frame++
    }
  }
}

export function Hero() {
  const elementRef = useRef<HTMLHeadingElement>(null)
  const scramblerRef = useRef<TextScramble | null>(null)
  const [mounted, setMounted] = useState(false)

  useEffect(() => {
    if (elementRef.current && !scramblerRef.current) {
      scramblerRef.current = new TextScramble(elementRef.current)
      setMounted(true)
    }
  }, [])

  useEffect(() => {
    if (mounted && scramblerRef.current) {
      // Type/scramble in once to "ClearTrade AI"
      scramblerRef.current.setText("ClearTrade AI")
    }
  }, [mounted])

  const handleChatClick = () => {
    const el = document.getElementById("advisor-bot")
    el?.scrollIntoView({ behavior: "smooth", block: "start" })
  }

  return (
    <header className="relative isolate min-h-[70vh] flex items-center justify-center overflow-hidden">
      <div className={cn("px-6 py-24 text-center")}>
        {/* match the previous 'typed' title look: monospace, bolder, wider tracking, larger size */}
        <h1
          ref={elementRef}
          className="text-white text-5xl md:text-7xl font-bold tracking-wider text-balance type-caret"
          style={{ fontFamily: "monospace" }}
        >
          {/* Scrambler will set text to ClearTrade AI */}
        </h1>
        <span className="sr-only">ClearTrade AI</span>

        <div className="mt-8 flex items-center justify-center">
          <Button size="lg" onClick={handleChatClick} aria-label="Open chat">
            Chat
          </Button>
        </div>
      </div>

      {/* Ensure scramble dud chars are visible in hero as neon green */}
      <style jsx global>{`
        .dud {
          color: #0f0;
          opacity: 0.7;
        }
        .type-caret::after {
          content: "▌";
          margin-left: 0.25rem;
          color: #0f0;
          animation: caret-blink 1s step-start infinite;
        }
        @keyframes caret-blink {
          50% {
            opacity: 0;
          }
        }
      `}</style>
    </header>
  )
}
