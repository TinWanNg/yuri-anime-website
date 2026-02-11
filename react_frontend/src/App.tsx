import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import Newest from './pages/Newest';
import './style.css';

createRoot(document.getElementById('root')!).render(
  <StrictMode>
    <Newest />
  </StrictMode>
);
