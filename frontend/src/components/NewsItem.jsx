import React from 'react';

const NewsItem = (props) => {
    return (
        <div className="news">
            <div className="news__content">
                <strong>{props.news.id}. {props.news.content}</strong>
                <div>
                    {props.news.url}
                </div>
            </div>
        </div>
    );
};

export default NewsItem;