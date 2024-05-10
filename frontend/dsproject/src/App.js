// App.js

import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import MainLayout from './pages/MainLayout';
import Home from './pages/Home';
import GamePrediction from './pages/GamePrediction';
import Analysis from './pages/Analysis';
import GameComparing from './pages/GameComparing';
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<MainLayout />}>
          <Route index element={<Home />} />
          <Route path="/gameprediction" element={<GamePrediction />} />
          <Route path="/analysis" element={<Analysis />} />
          <Route path="/gamecomparing" element={<GameComparing />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}

export default App;
