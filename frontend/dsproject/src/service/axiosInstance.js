import axios from 'axios';
const qs = require('qs')

const axiosInstance = axios.create({
    baseURL: 'http://127.0.0.1:8000',
    paramsSerializer: function (params) {
      return qs.stringify(params, { encode:false})
    },
  });

export default axiosInstance;