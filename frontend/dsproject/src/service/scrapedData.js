import axiosInstance from "./axiosInstance";


async function get(searchText, page){
    const {data}= await axiosInstance({
        method: 'GET',
        url: '/scraped-data',
        params: {searchText, page}
    })
    console.log(data);
    return data
}

export default {get}