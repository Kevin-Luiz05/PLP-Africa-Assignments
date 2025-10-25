import React from 'react'

export default function Footer() {
  return (
    <footer className="bg-white dark:bg-slate-900 border-t dark:border-t-slate-800">
      <div className="container mx-auto px-4 py-6 text-center text-sm text-gray-600 dark:text-gray-300">
        © {new Date().getFullYear()} PLP MERN — Built with React & Tailwind • <a className="text-primary" href="https://plp.africa">PLP Africa</a>
      </div>
    </footer>
  )
}
