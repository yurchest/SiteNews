import React, {useEffect, useState} from "react";
import NewsItem from "./NewsItem";
import {useFetching} from "../hooks/useFetching";
import YurchestService from "../API/YurchestService";
import NewsList from "./NewsList";
  
const Home = () => {

    const [news, setNews] = useState([])

    const [fetchNews, isNewsLoading, newsError] = useFetching(async() => {
        const response = await YurchestService.getAll();
        setNews(response.data)
    })

    useEffect(() => {
        fetchNews()
    }, [])


    return (
    <div>
        <h1>Its a home page</h1>
        <NewsList news = {news}/>
    </div>
  );
};
  
export default Home;