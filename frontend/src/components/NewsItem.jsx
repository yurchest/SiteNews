import React from 'react';

const NewsItem = (props) => {
    return (
        <div className="news">
            <div className="news__content">
                <strong>{props.news.id}. {props.news.content}</strong>
                <div>
                    <a href={props.news.url}>{props.news.url}</a>
                </div>
                <div>
                    {new Date(props.news.time_update).toLocaleString()}
                </div>
            </div>
        </div>
    );
};

export default NewsItem;