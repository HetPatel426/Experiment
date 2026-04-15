"use client"

import { WebGLShader } from "@/components/ui/web-gl-shader"
import { LiquidButton } from "@/components/ui/liquid-glass-button"
import { Spotlight } from "@/components/ui/spotlight"
import { SplineScene } from "@/components/ui/splite"
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
  CardDescription,
} from "@/components/ui/card"

export default function Portfolio() {
  return (
    <main className="bg-black text-white">
      {/* ───────────────────────── HERO ───────────────────────── */}
      <section className="relative flex min-h-screen w-full flex-col items-center justify-center overflow-hidden">
        {/* WebGL shader background */}
        <WebGLShader />

        {/* Spotlight */}
        <Spotlight
          className="-top-40 left-0 md:-top-20 md:left-60"
          fill="white"
        />

        {/* Content overlay */}
        <div className="relative z-10 flex w-full max-w-6xl flex-col items-center gap-8 px-4 md:flex-row md:items-stretch">
          {/* Left panel */}
          <div className="w-full md:w-1/2">
            <div className="border border-[#27272a] p-2">
              <div className="border border-[#27272a] py-10 px-6 overflow-hidden">
                <h1 className="mb-3 text-white text-center text-7xl font-extrabold tracking-tighter md:text-[clamp(2rem,8vw,7rem)]">
                  Het Patel
                </h1>
                <p className="text-white/60 text-center text-xs md:text-sm lg:text-base">
                  Cybersecurity &amp; IT Security Intern&nbsp;·&nbsp;Ohio
                  Department of Insurance
                </p>
                <p className="mt-2 text-white/40 text-center text-xs">
                  CompTIA A+ candidate. Pursuing incident response &amp; digital
                  forensics.
                </p>

                {/* Availability badge */}
                <div className="my-6 flex items-center justify-center gap-1">
                  <span className="relative flex h-3 w-3 items-center justify-center">
                    <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-green-500 opacity-75" />
                    <span className="relative inline-flex h-2 w-2 rounded-full bg-green-500" />
                  </span>
                  <p className="text-xs text-green-500">
                    Available for opportunities
                  </p>
                </div>

                <div className="flex justify-center">
                  <LiquidButton
                    className="text-white border border-zinc-700 rounded-full"
                    size="xl"
                    onClick={() =>
                      document
                        .getElementById("projects")
                        ?.scrollIntoView({ behavior: "smooth" })
                    }
                  >
                    View my work
                  </LiquidButton>
                </div>
              </div>
            </div>
          </div>

          {/* Right panel — Spline 3D */}
          <div className="relative hidden md:flex w-full md:w-1/2 items-center justify-center min-h-[420px]">
            <SplineScene
              scene="https://prod.spline.design/kZDDjO5HuC9GJUM2/scene.splinecode"
              className="h-full w-full"
            />
          </div>
        </div>
      </section>

      {/* ───────────────────────── ABOUT ───────────────────────── */}
      <section id="about" className="bg-zinc-950 py-24 px-6">
        <div className="mx-auto max-w-3xl">
          <h2 className="mb-8 font-mono text-3xl font-bold tracking-tight">
            About
          </h2>
          <p className="text-zinc-300 leading-relaxed text-base md:text-lg">
            I&apos;m studying Cybersecurity at Purdue Global (expected February
            2028). As an IT Security Intern at the Ohio Department of Insurance,
            I run Qualys VMDR vulnerability scans, remediate BIOS CVEs on HP
            EliteBook G9 laptops (sp168850.exe via PDQ Deploy), and help
            maintain endpoint protection across the organisation.
          </p>
          <p className="mt-4 text-zinc-400 leading-relaxed text-base md:text-lg">
            Long-term, I want to specialise in incident response and digital
            forensics. Outside of work I stay sharp on TryHackMe and build
            personal projects that sharpen my scripting and web-security skills.
          </p>
        </div>
      </section>

      {/* ───────────────────────── SKILLS ───────────────────────── */}
      <section id="skills" className="bg-black py-24 px-6">
        <div className="mx-auto max-w-5xl">
          <h2 className="mb-12 font-mono text-3xl font-bold tracking-tight">
            Skills
          </h2>
          <div className="grid gap-6 sm:grid-cols-2">
            <Card>
              <CardHeader>
                <CardTitle className="font-mono text-sm tracking-widest uppercase text-zinc-400">
                  Security &amp; Tools
                </CardTitle>
              </CardHeader>
              <CardContent>
                <ul className="space-y-1 text-sm text-zinc-300">
                  {[
                    "Qualys VMDR",
                    "PDQ Deploy",
                    "Endpoint protection",
                    "Vulnerability scanning",
                    "pfSense",
                  ].map((s) => (
                    <li key={s} className="flex items-center gap-2">
                      <span className="h-1 w-1 rounded-full bg-zinc-500" />
                      {s}
                    </li>
                  ))}
                </ul>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle className="font-mono text-sm tracking-widest uppercase text-zinc-400">
                  Networking
                </CardTitle>
              </CardHeader>
              <CardContent>
                <ul className="space-y-1 text-sm text-zinc-300">
                  {[
                    "TCP/IP",
                    "LAN / WAN / DMZ",
                    "NAT & DNS",
                    "Routing & switching",
                    "Ports & protocols",
                  ].map((s) => (
                    <li key={s} className="flex items-center gap-2">
                      <span className="h-1 w-1 rounded-full bg-zinc-500" />
                      {s}
                    </li>
                  ))}
                </ul>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle className="font-mono text-sm tracking-widest uppercase text-zinc-400">
                  Development
                </CardTitle>
              </CardHeader>
              <CardContent>
                <ul className="space-y-1 text-sm text-zinc-300">
                  {["Python", "React / Vite", "Tailwind CSS", "TypeScript"].map(
                    (s) => (
                      <li key={s} className="flex items-center gap-2">
                        <span className="h-1 w-1 rounded-full bg-zinc-500" />
                        {s}
                      </li>
                    )
                  )}
                </ul>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle className="font-mono text-sm tracking-widest uppercase text-zinc-400">
                  Certifications
                </CardTitle>
              </CardHeader>
              <CardContent>
                <ul className="space-y-1 text-sm text-zinc-300">
                  {[
                    "CompTIA A+ (in progress)",
                    "Security+ (planned)",
                    "CySA+ (planned)",
                  ].map((s) => (
                    <li key={s} className="flex items-center gap-2">
                      <span className="h-1 w-1 rounded-full bg-zinc-500" />
                      {s}
                    </li>
                  ))}
                </ul>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* ───────────────────────── PROJECTS ───────────────────────── */}
      <section id="projects" className="bg-zinc-950 py-24 px-6">
        <div className="mx-auto max-w-5xl">
          <h2 className="mb-12 font-mono text-3xl font-bold tracking-tight">
            Projects
          </h2>
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
            <Card>
              <CardHeader>
                <CardTitle>ALICE</CardTitle>
                <CardDescription>NBA Analysis Dashboard</CardDescription>
              </CardHeader>
              <CardContent>
                <p className="text-zinc-400 text-sm mb-3">
                  Interactive stat dashboard built with React, Vite, and Tailwind
                  CSS. Implements SHA-256 hashing, XOR-obfuscated API keys, and
                  session tokens for secure data access.
                </p>
                <div className="flex flex-wrap gap-1">
                  {["React", "Vite", "Tailwind", "SHA-256"].map((t) => (
                    <span
                      key={t}
                      className="rounded border border-zinc-700 px-2 py-0.5 text-xs text-zinc-400"
                    >
                      {t}
                    </span>
                  ))}
                </div>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle>F1 2026 Season Predictor</CardTitle>
                <CardDescription>GitHub Pages Web App</CardDescription>
              </CardHeader>
              <CardContent>
                <p className="text-zinc-400 text-sm mb-3">
                  Machine-learning-assisted predictor for the 2026 Formula 1
                  season, deployed as a static site on GitHub Pages.
                </p>
                <div className="flex flex-wrap gap-1">
                  {["Python", "GitHub Pages", "ML"].map((t) => (
                    <span
                      key={t}
                      className="rounded border border-zinc-700 px-2 py-0.5 text-xs text-zinc-400"
                    >
                      {t}
                    </span>
                  ))}
                </div>
              </CardContent>
            </Card>

            <Card>
              <CardHeader>
                <CardTitle>Python Security Tools</CardTitle>
                <CardDescription>Built from scratch</CardDescription>
              </CardHeader>
              <CardContent>
                <p className="text-zinc-400 text-sm mb-3">
                  Collection of CLI tools written in pure Python: a
                  cryptographically secure password generator, a quiz game, and a
                  hangman game.
                </p>
                <div className="flex flex-wrap gap-1">
                  {["Python", "CLI", "Security"].map((t) => (
                    <span
                      key={t}
                      className="rounded border border-zinc-700 px-2 py-0.5 text-xs text-zinc-400"
                    >
                      {t}
                    </span>
                  ))}
                </div>
              </CardContent>
            </Card>
          </div>
        </div>
      </section>

      {/* ───────────────────────── EXPERIENCE ───────────────────────── */}
      <section id="experience" className="bg-black py-24 px-6">
        <div className="mx-auto max-w-3xl">
          <h2 className="mb-12 font-mono text-3xl font-bold tracking-tight">
            Experience
          </h2>

          <ol className="relative border-l border-zinc-800">
            {[
              {
                date: "Apr 2025 – Present",
                role: "College Intern — IT Systems & Security",
                org: "Ohio Department of Insurance",
                desc: "Vulnerability scanning with Qualys VMDR, BIOS CVE remediation on HP EliteBook G9 (sp168850.exe via PDQ Deploy), and endpoint protection management.",
              },
              {
                date: "Prior",
                role: "Technology Sales & Support Associate",
                org: "Micro Center",
                desc: "Advised customers on hardware and software purchases, performed hands-on diagnostics and repairs across consumer and enterprise devices.",
              },
              {
                date: "Expected Feb 2028",
                role: "B.S. Cybersecurity",
                org: "Purdue Global",
                desc: "Coursework covering network security, digital forensics, incident response, and risk management.",
              },
            ].map((item) => (
              <li key={item.role} className="mb-10 ml-6">
                <span className="absolute -left-1.5 flex h-3 w-3 rounded-full border border-zinc-700 bg-zinc-900" />
                <time className="mb-1 text-xs font-mono text-zinc-500">
                  {item.date}
                </time>
                <h3 className="text-base font-semibold text-white">
                  {item.role}
                </h3>
                <p className="text-sm text-zinc-400">{item.org}</p>
                <p className="mt-1 text-sm text-zinc-500">{item.desc}</p>
              </li>
            ))}
          </ol>
        </div>
      </section>

      {/* ───────────────────────── CONTACT ───────────────────────── */}
      <section id="contact" className="bg-zinc-950 py-24 px-6">
        <div className="mx-auto max-w-xl text-center">
          <h2 className="mb-4 font-mono text-3xl font-bold tracking-tight">
            Contact
          </h2>
          <p className="mb-10 text-zinc-400 leading-relaxed">
            I&apos;m open to internships and entry-level roles in cybersecurity.
            Whether you have a project in mind or just want to connect, feel free
            to reach out.
          </p>
          <div className="flex flex-wrap items-center justify-center gap-3">
            <a
              href="https://linkedin.com/in/hetpatel426"
              target="_blank"
              rel="noopener noreferrer"
              className="rounded-full border border-zinc-700 px-5 py-2 text-sm text-zinc-300 transition hover:border-zinc-500 hover:text-white"
            >
              LinkedIn
            </a>
            <a
              href="https://github.com/hetpatel426"
              target="_blank"
              rel="noopener noreferrer"
              className="rounded-full border border-zinc-700 px-5 py-2 text-sm text-zinc-300 transition hover:border-zinc-500 hover:text-white"
            >
              GitHub
            </a>
            <a
              href="mailto:hetpatel426@outlook.com"
              className="rounded-full border border-zinc-700 px-5 py-2 text-sm text-zinc-300 transition hover:border-zinc-500 hover:text-white"
            >
              Email
            </a>
          </div>
        </div>
      </section>
    </main>
  )
}
