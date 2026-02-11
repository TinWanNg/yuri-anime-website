import type { ReactNode } from "react";
import Navbar from "./Navbar";

interface LayoutProps {
  children: ReactNode;
}

export default function Layout({ children }: LayoutProps) {
  return (
    <div className="relative min-h-screen text-white font-sans">
      {/* Background image */}
      <div
        className="absolute inset-0 bg-cover bg-center blur-sm brightness-50"
        style={{ backgroundImage: "url('/background.png')" }}
      />

      {/* Overlay */}
      <div className="absolute inset-0 bg-black/30" />

      {/* Content */}
      <div className="relative z-10">
        <Navbar />
        <main className="p-10">
          {children}
        </main>
      </div>
    </div>
  );
}
