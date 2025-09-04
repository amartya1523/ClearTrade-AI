"use client"

import { useState } from "react"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Textarea } from "@/components/ui/textarea"

export function AdvisorBot() {
  const [question, setQuestion] = useState("Is XYZ stock safe for long-term?")
  const [answer, setAnswer] = useState(
    "Based on risk signals and news, XYZ shows moderate risk. Consider diversified ETFs for long-term stability.",
  )

  return (
    <Card>
      <CardHeader>
        <CardTitle>Personalized Advisor Bot</CardTitle>
      </CardHeader>
      <CardContent className="grid gap-4">
        <Textarea
          value={question}
          onChange={(e) => setQuestion(e.target.value)}
          placeholder="Ask: Is XYZ stock safe?"
          aria-label="Advisor question"
        />
        <div className="flex gap-3">
          <Button onClick={() => setAnswer(answer)}>Ask</Button>
          <Button variant="secondary">Clear</Button>
        </div>
        <div className="rounded-md border p-3">
          <p className="text-sm">{answer}</p>
          <p className="text-xs text-muted-foreground mt-2">
            Disclaimer: This is not investment advice. Please do your own research. SEBI-compliant guidance applies.
          </p>
        </div>
      </CardContent>
    </Card>
  )
}
