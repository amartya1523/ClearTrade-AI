import type React from "react"

type SectionProps = {
  id: string
  title: string
  subtitle?: string
  children: React.ReactNode
}

export function Section({ id, title, subtitle, children }: SectionProps) {
  return (
    <section id={id} className="w-full py-12 md:py-16">
      <div className="container mx-auto px-6 max-w-5xl">
        <header className="mb-8 md:mb-10">
          <h2 className="text-2xl md:text-3xl font-semibold text-pretty">{title}</h2>
          {subtitle ? <p className="text-sm md:text-base text-muted-foreground mt-2 max-w-2xl">{subtitle}</p> : null}
        </header>
        {children}
      </div>
    </section>
  )
}
