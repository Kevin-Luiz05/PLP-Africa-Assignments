import React, { useEffect, useState } from 'react'
import Card from '../components/Card'
import Button from '../components/Button'
import useLocalStorage from '../hooks/useLocalStorage'

export default function Tasks() {
  const [tasks, setTasks] = useLocalStorage('plp_tasks', [
    { id: 1, text: 'Finish PLP assignment', done: false }
  ])
  const [text, setText] = useState('')
  const [filter, setFilter] = useState('all')

  function addTask() {
    if (!text.trim()) return
    setTasks([...tasks, { id: Date.now(), text: text.trim(), done: false }])
    setText('')
  }
  function toggle(id) {
    setTasks(tasks.map(t => t.id === id ? { ...t, done: !t.done } : t))
  }
  function remove(id) {
    setTasks(tasks.filter(t => t.id !== id))
  }

  const filtered = tasks.filter(t => {
    if (filter === 'active') return !t.done
    if (filter === 'completed') return t.done
    return true
  })

  return (
    <div className="max-w-2xl mx-auto">
      <Card>
        <h2 className="text-xl font-bold mb-3">Task Manager</h2>
        <div className="flex gap-2 mb-3">
          <input value={text} onChange={e => setText(e.target.value)} className="flex-1 p-2 border rounded" placeholder="New task" />
          <Button onClick={addTask}>Add</Button>
        </div>

        <div className="flex gap-2 mb-4">
          <Button variant={filter==='all'?'primary':'secondary'} onClick={()=>setFilter('all')}>All</Button>
          <Button variant={filter==='active'?'primary':'secondary'} onClick={()=>setFilter('active')}>Active</Button>
          <Button variant={filter==='completed'?'primary':'secondary'} onClick={()=>setFilter('completed')}>Completed</Button>
        </div>

        <ul className="space-y-2">
          {filtered.length === 0 && <div className="text-gray-500">No tasks</div>}
          {filtered.map(t => (
            <li key={t.id} className="flex items-center justify-between bg-card p-2 rounded">
              <div className="flex items-center gap-3">
                <input type="checkbox" checked={t.done} onChange={()=>toggle(t.id)} />
                <span className={t.done ? 'line-through text-gray-500' : ''}>{t.text}</span>
              </div>
              <div>
                <Button variant="danger" onClick={()=>remove(t.id)}>Delete</Button>
              </div>
            </li>
          ))}
        </ul>
      </Card>
    </div>
  )
}
