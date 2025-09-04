"use client"
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Label } from "@/components/ui/label"
import { Input } from "@/components/ui/input"
import { Select, SelectTrigger, SelectValue, SelectContent, SelectItem } from "@/components/ui/select"
import { RadioGroup, RadioGroupItem } from "@/components/ui/radio-group"
import { Button } from "@/components/ui/button"

export function OnboardingForm() {
  return (
    <Card>
      <CardHeader>
        <CardTitle>Investor Onboarding</CardTitle>
      </CardHeader>
      <CardContent className="grid gap-6">
        <div className="grid md:grid-cols-3 gap-4">
          <div className="grid gap-2">
            <Label htmlFor="name">Full Name</Label>
            <Input id="name" placeholder="Enter your name" />
          </div>
          <div className="grid gap-2">
            <Label htmlFor="age">Age</Label>
            <Input id="age" type="number" placeholder="e.g., 30" />
          </div>
          <div className="grid gap-2">
            <Label>Income Range</Label>
            <Select>
              <SelectTrigger aria-label="Income range">
                <SelectValue placeholder="Select range" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="lt5">Below ₹5L</SelectItem>
                <SelectItem value="5to10">₹5L–₹10L</SelectItem>
                <SelectItem value="10to25">₹10L–₹25L</SelectItem>
                <SelectItem value="gt25">Above ₹25L</SelectItem>
              </SelectContent>
            </Select>
          </div>
        </div>

        <div className="grid md:grid-cols-2 gap-4">
          <div className="grid gap-2">
            <Label>Investment Experience</Label>
            <Select>
              <SelectTrigger aria-label="Investment experience">
                <SelectValue placeholder="Select experience" />
              </SelectTrigger>
              <SelectContent>
                <SelectItem value="none">None</SelectItem>
                <SelectItem value="basic">Basic</SelectItem>
                <SelectItem value="intermediate">Intermediate</SelectItem>
                <SelectItem value="advanced">Advanced</SelectItem>
              </SelectContent>
            </Select>
          </div>
          <div className="grid gap-2">
            <Label>Risk Appetite</Label>
            <RadioGroup defaultValue="moderate" className="flex items-center gap-6">
              <div className="flex items-center space-x-2">
                <RadioGroupItem value="low" id="risk-low" />
                <Label htmlFor="risk-low">Low</Label>
              </div>
              <div className="flex items-center space-x-2">
                <RadioGroupItem value="moderate" id="risk-moderate" />
                <Label htmlFor="risk-moderate">Moderate</Label>
              </div>
              <div className="flex items-center space-x-2">
                <RadioGroupItem value="high" id="risk-high" />
                <Label htmlFor="risk-high">High</Label>
              </div>
            </RadioGroup>
          </div>
        </div>

        <div className="text-sm text-muted-foreground">Future: Integrate DigiLocker / Aadhaar eKYC.</div>

        <div className="flex justify-end">
          <Button>Save Profile</Button>
        </div>
      </CardContent>
    </Card>
  )
}
