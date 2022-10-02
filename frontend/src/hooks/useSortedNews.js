import {useMemo} from 'react'


export const useSortedNews = (news) => {
    const sortedNews = useMemo(() => {
        return [...news].sort((a, b) => Date.parse(b.time_update) - Date.parse(a.time_update))
    }, [news])
    return sortedNews;
}