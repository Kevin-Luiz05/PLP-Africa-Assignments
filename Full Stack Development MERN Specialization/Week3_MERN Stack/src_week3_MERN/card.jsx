import React from 'react'

export default function Card({ children, className = '' }) {
  return (
    <div className={`bg-card border border-gray-200 dark:border-gray-700 shadow-sm rounded p-4 ${className}`}>
      {children}
    </div>
  )
}
