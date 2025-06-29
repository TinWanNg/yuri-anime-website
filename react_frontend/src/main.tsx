import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './style.css'
import Newest from './Newest.tsx'

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Newest />
  </StrictMode>,
)
