function sendRequest(method, url, data) {
    let config = {
        method: method,
        url: url,
        data: data,
        xsrfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFToken',
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    }
    return  axios(config)
}

Vue.createApp({
    data() {
        return {
            task: '',
            tasks: [
                {title: 'one'},
                {title: 'two'}
            ]
        }
    },
    methods: {
        createTask() {
            let formData = new FormData();
            formData.append('title', this.task);
            sendRequest('post', '', formData)
                .then( (response) => {
                    this.tasks.unshift(response.data.task);
                    this.task = '';
                })
        },
        completeTask(taskId, index) {
            sendRequest('post', '' + taskId + '/complete/')
                .then( (response) => {
                    this.tasks.splice(index, 1);
                    this.tasks.push(response.data.task);
                })
        },
        deleteTask(taskId, index) {
            sendRequest('post', '' + taskId + '/delete/')
                .then(( response ) => {
                    this.tasks.splice(index, 1);
            })
        }
    },
    created() {
        let vm = this;
        let r = sendRequest('get', '')
            .then( ( response ) => {
                this.tasks = response.data.tasks;
            })
    }

}).mount('#app')
