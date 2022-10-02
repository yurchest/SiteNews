import Navbar from "./components/UI/navbar/Navbar";
import "./styles/main.css"
import Home from "./components/Home"
import {
  Routes,
  Route,
} from "react-router-dom"
import NotFound from "./components/NotFound";

function App() {


  return (
   <>
      <Navbar/>
      <div>
        <Routes>  
          <Route path="/home" element={<Home/>}/>
            <Route path = "*" element={<NotFound/>}/>
        </Routes>
      </div>
   </>  
  );
}

export default App;
