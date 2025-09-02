"use client"

import { useState } from "react"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import { Button } from "@/components/ui/button"
import { Badge } from "@/components/ui/badge"
import { RadialBar, RadialBarChart, ResponsiveContainer } from "recharts"

export function RiskAnalyzer() {
  const [query, setQuery] = useState("")
  const risk = 68 // demo value
  const fill = risk < 40 ? "#22c55e" : risk < 70 ? "#eab308" : "#ef4444"

  return (
    <Card>
      <CardHeader>
        <CardTitle>Investment Risk Analyzer</CardTitle>
      </CardHeader>
      <CardContent className="grid gap-6">
        <div className="flex gap-3">
          <Input
            placeholder="Search stock or mutual fund (e.g., INFY, NIFTY ETF)"
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            aria-label="Search instrument"
          />
          <Button>Analyze</Button>
        </div>

        <div className="grid md:grid-cols-3 gap-6">
          <div className="md:col-span-1">
            <div className="h-48">
              <ResponsiveContainer width="100%" height="100%">
                <RadialBarChart
                  data={[{ name: "Risk", value: risk, fill }]}
                  innerRadius="60%"
                  outerRadius="90%"
                  startAngle={90}
                  endAngle={-270}
                >
                  <RadialBar minAngle={15} dataKey="value" clockWise cornerRadius={8} />
                </RadialBarChart>
              </ResponsiveContainer>
            </div>
            <div className="text-center mt-2">
              <div className="text-sm">AI Risk Score</div>
              <div className="text-lg font-semibold">{risk}/100</div>
              <Badge className="mt-1" variant={risk < 40 ? "default" : risk < 70 ? "secondary" : "destructive"}>
                {risk < 40 ? "Safe" : risk < 70 ? "Moderate" : "Risky"}
              </Badge>
            </div>
          </div>

          <div className="md:col-span-2 grid gap-4">
            <div>
              <h4 className="font-medium mb-2">Reasons & Insights</h4>
              <ul className="list-disc pl-5 text-sm text-muted-foreground space-y-1">
                <li>Elevated volatility over the last 2 weeks</li>
                <li>Negative news sentiment from multiple sources</li>
                <li>Unusual trading patterns vs historical baseline</li>
              </ul>
            </div>
            <div>
              <h4 className="font-medium mb-2">Safer Alternatives</h4>
              <div className="flex flex-wrap gap-2">
                <Badge>NIFTY 50 ETF</Badge>
                <Badge>SENSEX ETF</Badge>
                <Badge variant="secondary">Diversified Large-Cap MF</Badge>
                <Badge variant="secondary">Liquid Fund (Short-term)</Badge>
              </div>
            </div>
          </div>
        </div>
      </CardContent>
    </Card>
  )
}
