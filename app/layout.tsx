import type { Metadata } from "next";
import localFont from "next/font/local";
import "./globals.css";
import { cn } from "@/lib/utils";

const geistSans = localFont({
  src: "./fonts/GeistVF.woff",
  variable: "--font-geist-sans",
  weight: "100 900",
});

const geistMono = localFont({
  src: "./fonts/GeistMonoVF.woff",
  variable: "--font-geist-mono",
  weight: "100 900",
});

export const metadata: Metadata = {
  title: "Het Patel — Cybersecurity Portfolio",
  description:
    "Cybersecurity student and IT Security Intern at Ohio Department of Insurance. CompTIA A+ candidate pursuing incident response and digital forensics.",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html
      lang="en"
      className={cn(
        "scroll-smooth",
        geistSans.variable,
        geistMono.variable
      )}
    >
      <body
        className={cn(
          "antialiased bg-black text-white",
          geistSans.variable,
          geistMono.variable
        )}
      >
        {children}
      </body>
    </html>
  );
}
