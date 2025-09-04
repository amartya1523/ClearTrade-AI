"use client"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import { Pie, PieChart, Cell, ResponsiveContainer, Tooltip, Legend } from "recharts"

const COLORS = ["#22c55e", "#0ea5e9", "#eab308", "#ef4444"]

const allocation = [
  { name: "Large Cap", value: 45 },
  { name: "ETF", value: 30 },
  { name: "Debt/Liquid", value: 15 },
  { name: "Others", value: 10 },
]

export function ReportsCompliance() {
  return (
    <div className="grid gap-6 md:grid-cols-2">
      <Card>
        <CardHeader>
          <CardTitle>Weekly Risk Report</CardTitle>
        </CardHeader>
        <CardContent className="grid gap-4">
          <p className="text-sm text-muted-foreground">Download your weekly portfolio risk summary (PDF).</p>
          <Button>Download PDF</Button>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <CardTitle>Portfolio Diversification</CardTitle>
        </CardHeader>
        <CardContent className="h-64">
          <ResponsiveContainer width="100%" height="100%">
            <PieChart>
              <Pie data={allocation} dataKey="value" nameKey="name" innerRadius={60} outerRadius={80} paddingAngle={2}>
                {allocation.map((entry, index) => (
                  <Cell key={`cell-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
              <Legend />
            </PieChart>
          </ResponsiveContainer>
          <p className="text-xs text-muted-foreground mt-3">
            Educational tips are provided for diversification. SEBI-compliant disclaimers apply.
          </p>
        </CardContent>
      </Card>
    </div>
  )
}
