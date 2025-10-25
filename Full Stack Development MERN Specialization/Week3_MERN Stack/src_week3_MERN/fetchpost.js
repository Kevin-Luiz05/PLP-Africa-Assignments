const BASE = 'https://jsonplaceholder.typicode.com'

export async function fetchPosts(page = 1, limit = 10) {
  const res = await fetch(`${BASE}/posts?_page=${page}&_limit=${limit}`)
  if (!res.ok) throw new Error('Failed to fetch posts')
  const data = await res.json()
  return data
}
