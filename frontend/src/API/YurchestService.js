import axios from "axios";

export default class YurchestService {
    static async getAll() {
        // return await axios.get("/api/news/");
        return await axios.get("http://localhost:8000/api/news/");
    }
}
