"use client"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Badge } from "@/components/ui/badge"

export function NewsSocial() {
  return (
    <div className="grid gap-6 md:grid-cols-3">
      <Card className="md:col-span-2">
        <CardHeader>
          <CardTitle>News Sentiment</CardTitle>
        </CardHeader>
        <CardContent className="grid gap-4">
          <div className="flex items-start justify-between">
            <div>
              <p className="font-medium">Bluechip earnings beat expectations</p>
              <p className="text-sm text-muted-foreground">Source: Business Daily</p>
            </div>
            <Badge>Positive</Badge>
          </div>
          <div className="flex items-start justify-between">
            <div>
              <p className="font-medium">Sector rotation dampens mid-cap outlook</p>
              <p className="text-sm text-muted-foreground">Source: MarketWatch</p>
            </div>
            <Badge variant="secondary">Neutral</Badge>
          </div>
          <div className="flex items-start justify-between">
            <div>
              <p className="font-medium">Regulatory query sent to ABC Finserv</p>
              <p className="text-sm text-muted-foreground">Source: Exchange Filing</p>
            </div>
            <Badge variant="destructive">Negative</Badge>
          </div>
        </CardContent>
      </Card>

      <div className="grid gap-6">
        <Card>
          <CardHeader>
            <CardTitle>Social Buzz Tracker</CardTitle>
          </CardHeader>
          <CardContent className="text-sm text-muted-foreground">
            Spike detected for XYZ Corp: mentions up 240% vs 7-day avg.
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <CardTitle>Pump & Dump Alerts</CardTitle>
          </CardHeader>
          <CardContent>
            <div className="rounded-md border border-destructive/30 p-3">
              <p className="text-sm">
                High-risk pattern detected for ABC Ltd: price-volume anomaly and coordinated posts.
              </p>
            </div>
          </CardContent>
        </Card>
      </div>
    </div>
  )
}
