import s from './MainPage.module.css'
import mainImg from '../../assets/images/main-page-img.png'
import {NavLink} from "react-router-dom";

const MainPage = () => {
    return (
        <div className={s.mainPageRow}>
            <div className={s.textBlock}>
                <div className={s.text}>
                    We make <br/>comparison <br/> easier
                </div>
                <NavLink className={s.startButton} to={'/search'}>Start</NavLink>
            </div>
            <div className={s.imageContainer}>
                <img src={mainImg} alt="Main page img" className={s.mainImg}/>
            </div>
        </div>
    )


}
export default MainPage;
