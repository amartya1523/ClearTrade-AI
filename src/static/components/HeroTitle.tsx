"use client"

import { useEffect, useState } from "react"

const TARGET = "ClearTrade AI"

export function HeroTitle() {
  const [text, setText] = useState("")
  const [done, setDone] = useState(false)

  useEffect(() => {
    let i = 0
    const interval = setInterval(() => {
      setText(TARGET.slice(0, i + 1))
      i++
      if (i >= TARGET.length) {
        clearInterval(interval)
        setDone(true)
      }
    }, 60)
    return () => clearInterval(interval)
  }, [])

  return (
    <h1
      aria-label="ClearTrade AI"
      className="font-mono text-4xl md:text-6xl lg:text-7xl font-semibold tracking-tight text-foreground"
    >
      {text}
      {!done && <span className="animate-pulse">|</span>}
    </h1>
  )
}
