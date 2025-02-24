import React from 'react'
import ReactDOM from 'react-dom/client'
import './main.css'
import { BrowserRouter, Routes, Route} from 'react-router-dom'
import Home from './pages/home'
import Upload from './pages/upload'

function App() {
 return (
  <div>
    <BrowserRouter>
      <Routes>
        <Route index element={<Home />} />
        <Route path="/upload" element={<Upload />} />
      </Routes>
    </BrowserRouter>
  </div>
 )
}

ReactDOM.createRoot(document.getElementById('root')!).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
)