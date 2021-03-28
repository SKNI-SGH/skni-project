import s from './SearchPage.module.css'
const SearchPage = () => {
    return (
        <div className={s.searchPageRow}>
           <header className={s.header}>Type company name/ticker</header>
            <input type="text" className={s.input}/>
        </div>
    )
}
export default SearchPage;