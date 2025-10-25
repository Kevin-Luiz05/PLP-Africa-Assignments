import React from 'react'

export default function Button({ children, variant = 'primary', onClick, className = '' }) {
  const base = 'px-4 py-2 rounded font-semibold transition'
  const variants = {
    primary: 'bg-primary text-white hover:bg-blue-600',
    secondary: 'bg-gray-200 text-gray-800 hover:bg-gray-300',
    danger: 'bg-red-500 text-white hover:bg-red-600'
  }
  return (
    <button className={`${base} ${variants[variant] || variants.primary} ${className}`} onClick={onClick}>
      {children}
    </button>
  )
}
