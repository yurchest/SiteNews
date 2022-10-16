import React from "react";
import NewsItem from "./NewsItem";
import { CSSTransition, TransitionGroup } from "react-transition-group";

const NewsList = ({ news }) => {
    return (
        <div>
            <TransitionGroup>
                {news.map((current_news, index) => (
                    <CSSTransition
                        key={current_news.id}
                        timeout={500}
                        classNames="news"
                    >
                        <NewsItem news={current_news} />
                    </CSSTransition>
                ))}
            </TransitionGroup>
        </div>
    );
};

export default NewsList;
