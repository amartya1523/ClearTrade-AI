import RainingLetters from "../components/RainingLetters"
import { Hero } from "../components/cleartrade/Hero"
import { Section } from "../components/cleartrade/Section"
import { OnboardingForm } from "../components/cleartrade/OnboardingForm"
import { DashboardOverview } from "../components/cleartrade/DashboardOverview"
import { RiskAnalyzer } from "../components/cleartrade/RiskAnalyzer"
import { NewsSocial } from "../components/cleartrade/NewsSocial"
import { AdvisorBot } from "../components/cleartrade/AdvisorBot"
import { ReportsCompliance } from "../components/cleartrade/ReportsCompliance"

export default function Home() {
  return (
    <main className="relative min-h-screen bg-black">
      <RainingLetters showTitle={false} asBackground />

      <div className="relative z-10">
        <section>
          <Hero />
        </section>

        <Section
          id="onboarding"
          title="Investor Onboarding / Profile Setup"
          subtitle="Simple KYC form, risk appetite questionnaire, and future eKYC integration."
        >
          <OnboardingForm />
        </Section>

        <Section
          id="dashboard"
          title="Dashboard (Main Home Screen)"
          subtitle="Portfolio snapshot, risk meter, AI alerts, and market sentiment overview."
        >
          <DashboardOverview />
        </Section>

        <Section
          id="risk-analyzer"
          title="Investment Risk Analyzer"
          subtitle="Search any stock or fund to view AI risk score with reasons and safer alternatives."
        >
          <RiskAnalyzer />
        </Section>

        <Section
          id="news-social"
          title="News & Social Media Feed Analysis"
          subtitle="Real-time sentiment cards, social buzz tracking, and pump & dump alerts."
        >
          <NewsSocial />
        </Section>

        <Section
          id="advisor-bot"
          title="Personalized Advisor Bot (AI Chat)"
          subtitle="Ask safety questions or request long-term suggestions with a SEBI disclaimer."
        >
          <AdvisorBot />
        </Section>

        <Section
          id="reports-compliance"
          title="Reports & Compliance"
          subtitle="Weekly risk report download, diversification score, and compliance notes."
        >
          <ReportsCompliance />
        </Section>
      </div>
    </main>
  )
}
