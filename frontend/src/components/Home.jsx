import React, { useEffect, useState } from "react";
import NewsItem from "./NewsItem";
import { useFetching } from "../hooks/useFetching";
import YurchestService from "../API/YurchestService";
import NewsList from "./NewsList";
import { useSortedNews } from "../hooks/useSortedNews";

const Home = () => {
    const [news, setNews] = useState([]);

    const [fetchNews, isNewsLoading, newsError] = useFetching(async () => {
        const response = await YurchestService.getAll();
        setNews(response.data);
    });

    const sortedNews = useSortedNews(news);

    useEffect(() => {
        fetchNews();
    }, []);

    return (
        <div>
            <h1>Its a home page</h1>
            <NewsList news={sortedNews} />
        </div>
    );
};

export default Home;
