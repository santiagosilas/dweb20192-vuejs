/*eslint-disable */

export class HttpResource {
    constructor(route) {
        this.route = route;
    }
    get url() {
        return 'localhost:5000/api' + this.route;
    }
}