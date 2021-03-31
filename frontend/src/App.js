import logo from './logo.svg';
import './App.css';
import Header from "./components/Header/Header";
import {BrowserRouter} from "react-router-dom";
import {Route} from "react-router";
import MainPage from "./components/MainPage/MainPage";
import SearchPage from "./components/SearchPage/SearchPage";

function App() {
  return (
      <BrowserRouter>
    <div className="App">
     <Header />
     <Route  path={'/home'} component={MainPage}/>
     <Route path={'/search'} component={SearchPage} />
    </div>
      </BrowserRouter>
  );
}

export default App;
