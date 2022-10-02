import axios from "axios";

export default class YurchestService {
    static async getAll() {
        return await axios.get("/api/news/");
    }
}