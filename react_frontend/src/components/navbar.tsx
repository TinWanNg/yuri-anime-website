import React from "react";

export default function Layout() {
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
        {/* Navbar */}
        <nav className="relative flex items-center justify-between px-16 py-8">
          {/* Left Links */}
          <div className="flex items-center gap-[64px] text-color-1 text-[18px] font-medium font-poppins">
            <a href="#" className="hover:text-blue-300">Recommended</a>
            <a href="#" className="hover:text-blue-300">Newest</a>
            <a href="#" className="hover:text-blue-300">Genres</a>
          </div>

          {/* Center Logo (absolutely centered) */}
          <div className="absolute left-1/2 transform -translate-x-1/2 text-[32px] font-bold text-color-2 font-oswald">
            yurigarden.de
          </div>

          {/* Right Section */}
          <div className="flex items-center gap-[48px] text-color-1 text-[18px] font-medium font-poppins">
            {/* Search Icon */}
            <button className="w-6 h-6">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="w-6 h-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M21 21l-4.35-4.35m0 0A7.5 7.5 0 1116.65 5.65a7.5 7.5 0 010 10.6z" />
              </svg>
            </button>

            {/* Bell Icon */}
            <button className="w-6 h-6">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                className="w-6 h-6"
                fill="none"
                viewBox="0 0 24 24"
                stroke="currentColor"
              >
                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V4a2 2 0 10-4 0v1.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9" />
              </svg>
            </button>

            {/* Login Text */}
            <button className="hover:text-blue-300">Login</button>
          </div>
        </nav>


        {/* Page content placeholder */}
        <main className="p-10">
          <h1 className="text-4xl font-bold">TBA</h1>
        </main>
      </div>
    </div>
  );
}
