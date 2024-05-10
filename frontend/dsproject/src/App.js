import Home from './pages/Home';
import GamePrediction from './pages/GamePrediction';
import Analysis from './pages/Analysis';
import { BrowserRouter, Routes, Route } from "react-router-dom";
function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />}>
          <Route path="gameprediction" element={<GamePrediction />} />
          <Route path="analysis" element={<Analysis />} />
        </Route>
      </Routes>
    </BrowserRouter>
  );
}


export default App;
