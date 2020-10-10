import {store} from "../../store";
import {makeRequestError} from "../Error/requestError"

//массив со всеми клиентами
let arrayClient = [];

/**
 * преобразование ответа в JSON объект
 * @param response
 * @returns {[]}
 */
let parseReq = (response) => {
  for (let data of JSON.parse(response).data) {
    arrayClient.push({
      id: data.id,
      number: data.attributes.number,
      code: data.attributes.code,
      full_name: data.attributes.full_name,
    })
  }
  return arrayClient;
}

/**
 * склеивание данный клиента в строку
 * @param client - объект с данными клиента
 * @returns {{full: string}}
 */
let string = (client) => ({
  full: client.number + ' ' +
    client.code + ' ' +
    client.full_name
})

/**
 * функция поиска клиентов по строке
 * @param text - строка для поиска
 * @returns массив с клиентами, подъодящими под критерии
 */
export function searchText(text) {
  let bufArray = [];
  for (let client of arrayClient) {
    if (string(client).full.toLowerCase().includes(text.toLowerCase())) {
      bufArray.push(client);
    }
  }
  return bufArray;
}

/**
 * функция получение списка клиентов
 * @returns {Promise<Error or clientObject>}
 */
export function getClientList() {
  $.ajaxSetup({
          headers: {'Authorization': 'Token ' + localStorage.getItem('auth_token')}
  })
  return new Promise(function (resolve, reject) {
    let req = new XMLHttpRequest();
    req.open(
      'GET',
      store.state.baseUrl + store.state.clientsList,
      true
    );
    req.setRequestHeader('Authorization', 'Token ' + localStorage.getItem('auth_token'));
    req.send();

    req.onload = function () {
      if (this.status === 200) {
        resolve(parseReq(this.response));
      } else reject(makeRequestError(this));
    };

    req.onerror = function () {
      reject(new Error("Network Error"));
    };

  });
}
