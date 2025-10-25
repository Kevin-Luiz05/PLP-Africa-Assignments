import React from 'react'
import Card from '../components/Card'
import Button from '../components/Button'
import { Link } from 'react-router-dom'

export default function Home() {
  return (
    <div className="grid gap-6 md:grid-cols-2">
      <Card>
        <h2 className="text-2xl font-bold mb-2">Welcome</h2>
        <p className="mb-4">A responsive React app using Tailwind CSS. Use the Tasks page to manage tasks and the Posts page to fetch posts from JSONPlaceholder.</p>
        <Link to="/tasks"><Button>Open Task Manager</Button></Link>
      </Card>

      <Card>
        <h3 className="text-xl font-semibold mb-2">Features</h3>
        <ul className="list-disc pl-5 space-y-1">
          <li>Component architecture</li>
          <li>useState, useEffect, useContext</li>
          <li>LocalStorage persistence</li>
          <li>API integration, search & pagination</li>
        </ul>
      </Card>
    </div>
  )
}
