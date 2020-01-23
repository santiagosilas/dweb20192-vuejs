import { HttpService } from "./HttpService";

class ProjectService extends HttpService {
    constructor() {
        super("projects")
    }
}

export const projects = new ProjectService()