import React, { useEffect, useState } from 'react'
import Card from '../components/Card'
import Button from '../components/Button'
import { fetchPosts } from '../api/fetchPosts'

export default function APIList() {
  const [posts, setPosts] = useState([])
  const [page, setPage] = useState(1)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)
  const [query, setQuery] = useState('')

  useEffect(() => {
    let mounted = true
    setLoading(true)
    setError(null)
    fetchPosts(page, 10)
      .then(data => { if (mounted) setPosts(data) })
      .catch(err => { if (mounted) setError(err.message) })
      .finally(() => { if (mounted) setLoading(false) })
    return () => { mounted = false }
  }, [page])

  const filtered = posts.filter(p => p.title.includes(query) || p.body.includes(query))

  return (
    <div className="max-w-4xl mx-auto">
      <Card>
        <div className="flex items-center justify-between mb-4">
          <h2 className="text-xl font-bold">Posts (JSONPlaceholder)</h2>
          <div className="flex gap-2">
            <input value={query} onChange={e=>setQuery(e.target.value)} placeholder="Search" className="p-2 border rounded" />
            <Button onClick={()=>setPage(1)}>Search</Button>
          </div>
        </div>

        {loading && <div>Loading...</div>}
        {error && <div className="text-red-500">Error: {error}</div>}

        <ul className="space-y-3">
          {filtered.map(post => (
            <li key={post.id} className="bg-card p-3 rounded">
              <h3 className="font-semibold">{post.title}</h3>
              <p className="text-sm text-gray-600">{post.body}</p>
            </li>
          ))}
        </ul>

        <div className="flex gap-2 justify-center mt-4">
          <Button onClick={()=>setPage(p=>Math.max(1,p-1))} className="px-3">Prev</Button>
          <div className="px-3 py-2">Page {page}</div>
          <Button onClick={()=>setPage(p=>p+1)} className="px-3">Next</Button>
        </div>
      </Card>
    </div>
  )
}
