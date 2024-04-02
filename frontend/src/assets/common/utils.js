// /*
//  * @Author: HKini 1778267485@qq.com
//  * @Date: 2024-03-06 11:40:43
//  * @LastEditTime: 2024-03-06 11:41:15
//  * @LastEditors: HKini 1778267485@qq.com
//  * @Description: 前端使用到的工具函数
//  * @FilePath: \TimeCanvas\frontend\src\assets\common\utils.js
//  * 
//  */


import axios from 'axios'
import CryptoJS from 'crypto-js'
//获取百度网盘用户得access_token
export function getAccessToken() {
    return new Promise((resolve, reject) => {
        axios.get('/userinfo').then(res => {
            resolve(res.data)
        }).catch(err => {
            reject(err)
        })
    })
}
//
export function GetCookie(name) {
    const cookieArr = document.cookie.split(';');
    for (var i = 0; i < cookieArr.length; i++) {
        const temp = cookieArr[i].split("=")
      // 如果找到了名称匹配的cookie，返回它的值
      if (name == temp[0].trim()) {
        return decodeURIComponent(temp[1]);
      }
    }
    // 如果没有找到，返回null
    return null;
  }

//返回用户access_token,以及网盘会员等级
export function getUserInfo() {
    return new Promise((resolve, reject) => {
        axios.get('/userinfo').then(res => {
            let data = {
                access_token: res.data['access_token'],
                vip_type: res.data['vip_type']
            
            }
            let list=[]
            list.push(data)
            resolve(list)
            // resolve(res.data)
        }).catch(err => {
            reject(err)
        })
    })
}
//根据用户会员等级，限制用户可以上传文件的大小以及上传文件的类型
// 普通用户单个上传文件大小上限为4GB
// 会员用户单个上传文件大小上限为10GB
// 超级会员用户单个上传文件大小上限为20GB
// 普通用户无法上传视频、Live Photo类型的文件。
export function getLimit(vip_type) {
    let limit = {
        size: 4,
        type: ['video', 'livephoto']
    }
    if (vip_type == 1) {
        limit.size = 10
    } else if (vip_type == 2) {
        limit.size = 20
    }
    return limit
}
//判断文件大小，对超过4M的文件进行分片，并用list返回所有分片的md5值
export function getMd5(file, size) {
    let list = []
    let chunks = Math.ceil(file.size / size)
    for (let i = 0; i < chunks; i++) {
        let start = i * size
        let end = Math.min(file.size, start + size)
        let blob = file.slice(start, end)
        let reader = new FileReader()
        reader.readAsArrayBuffer(blob)
        reader.onload = function (e) {
            let spark = new SparkMD5.ArrayBuffer()
            spark.append(e.target.result)
            list.push(spark.end())
        }
    }
    return list
}
//计算一个文件的md5值
// 在 JavaScript 中，FileReader 的 readAsArrayBuffer 方法是异步的，这意味着它不会立即返回结果。
// 相反，它会在后台读取文件，然后在完成时触发 onload 事件。
// 因此，我们不能立即获取到 MD5 值，而需要使用 Promise 来处理这种异步操作。
export function calculateMD5(file) {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
  
      reader.onload = function(event) {
        const data = event.target.result;
        const wordArray = CryptoJS.lib.WordArray.create(data);
        const hash = CryptoJS.MD5(wordArray);
        resolve(hash.toString());
      };
  
      reader.onerror = function(event) {
        reject(new Error("读取文件失败"));
      };
      reader.readAsArrayBuffer(file);
    });
  }
