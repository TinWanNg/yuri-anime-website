import { useState } from 'react'
import Navbar from './components/navbar';

function Newest() {
  const [count, setCount] = useState(0)

  return (
    <Navbar />
  )
}

export default Newest
