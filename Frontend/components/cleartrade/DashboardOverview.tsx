"use client"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import { RadialBar, RadialBarChart, ResponsiveContainer, Tooltip } from "recharts"

const holdings = [
  { asset: "NIFTY 50 ETF", type: "ETF", qty: 10, value: "₹18,500" },
  { asset: "Axis Bluechip", type: "Mutual Fund", qty: 120, value: "₹32,000" },
  { asset: "TCS", type: "Stock", qty: 5, value: "₹18,200" },
]

const riskData = [{ name: "Risk", value: 42, fill: "#22c55e" }] // green-ish for demo

const sentimentGrid = [
  ["pos", "pos", "neu", "neg", "pos", "neu"],
  ["neg", "neu", "pos", "pos", "neu", "neg"],
  ["pos", "pos", "pos", "neu", "neg", "pos"],
]

function cellColor(code: string) {
  if (code === "pos") return "bg-emerald-500/70"
  if (code === "neg") return "bg-rose-500/70"
  return "bg-zinc-500/50"
}

export function DashboardOverview() {
  return (
    <div className="grid gap-6 md:grid-cols-5">
      <Card className="md:col-span-3">
        <CardHeader>
          <CardTitle>Portfolio Snapshot</CardTitle>
        </CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>Asset</TableHead>
                <TableHead>Type</TableHead>
                <TableHead className="text-right">Qty</TableHead>
                <TableHead className="text-right">Value</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {holdings.map((h) => (
                <TableRow key={h.asset}>
                  <TableCell>{h.asset}</TableCell>
                  <TableCell>{h.type}</TableCell>
                  <TableCell className="text-right">{h.qty}</TableCell>
                  <TableCell className="text-right">{h.value}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>

      <div className="grid gap-6 md:col-span-2">
        <Card>
          <CardHeader>
            <CardTitle>Risk Meter</CardTitle>
          </CardHeader>
          <CardContent className="h-48">
            <ResponsiveContainer width="100%" height="100%">
              <RadialBarChart data={riskData} innerRadius="60%" outerRadius="90%" startAngle={90} endAngle={-270}>
                <RadialBar minAngle={15} dataKey="value" clockWise cornerRadius={8} />
                <Tooltip />
              </RadialBarChart>
            </ResponsiveContainer>
            <div className="mt-2 text-center text-sm text-muted-foreground">Overall Portfolio Risk: 42/100</div>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>AI Alerts</CardTitle>
          </CardHeader>
          <CardContent className="grid gap-3">
            <div className="flex items-start justify-between">
              <div>
                <p className="font-medium">Pump & Dump Warning - ABC Ltd</p>
                <p className="text-sm text-muted-foreground">Unusual volume spike and coordinated mentions detected.</p>
              </div>
              <Badge variant="destructive">High</Badge>
            </div>
            <div className="flex items-start justify-between">
              <div>
                <p className="font-medium">Misinformation Flag</p>
                <p className="text-sm text-muted-foreground">Conflicting earnings rumors; official filing pending.</p>
              </div>
              <Badge>Moderate</Badge>
            </div>
          </CardContent>
        </Card>
      </div>

      <Card className="md:col-span-5">
        <CardHeader>
          <CardTitle>Market Sentiment Overview</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-6 gap-2">
            {sentimentGrid.flatMap((row, rIdx) =>
              row.map((cell, cIdx) => (
                <div
                  key={`${rIdx}-${cIdx}`}
                  className={`h-6 rounded ${cellColor(cell)}`}
                  aria-label={`cell ${rIdx + 1}-${cIdx + 1}`}
                />
              )),
            )}
          </div>
          <p className="text-xs text-muted-foreground mt-3">Green = Positive, Red = Negative, Gray = Neutral</p>
        </CardContent>
      </Card>
    </div>
  )
}
