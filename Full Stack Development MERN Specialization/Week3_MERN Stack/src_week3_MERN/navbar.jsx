import React from 'react'
import { Link } from 'react-router-dom'
import { useTheme } from '../context/ThemeContext'
import Button from './button'

export default function Navbar() {
  const { dark, setDark } = useTheme()
  return (
    <nav className="bg-white dark:bg-slate-900 border-b dark:border-b-slate-800">
      <div className="container mx-auto px-4 py-3 flex items-center justify-between">
        <div className="flex items-center gap-4">
          <Link to="/" className="text-xl font-bold text-primary">PLP MERN</Link>
          <Link to="/tasks" className="text-sm text-gray-600 dark:text-gray-300">Tasks</Link>
          <Link to="/posts" className="text-sm text-gray-600 dark:text-gray-300">Posts</Link>
        </div>
        <div className="flex items-center gap-3">
          <Button variant="secondary" onClick={() => setDark(!dark)}>
            {dark ? 'Light' : 'Dark'}
          </Button>
        </div>
      </div>
    </nav>
  )
}
