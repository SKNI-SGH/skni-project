import logo from './logo.svg';
import './App.css';
import Header from "./components/Header/Header";
import {BrowserRouter} from "react-router-dom";
import {Route} from "react-router";
import MainPage from "./components/MainPage/MainPage";

function App() {
  return (
      <BrowserRouter>
    <div className="App">
     <Header />
     <Route  path={'/home'} component={MainPage}/>
    </div>
      </BrowserRouter>
  );
}

export default App;
