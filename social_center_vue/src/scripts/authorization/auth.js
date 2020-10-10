import {store} from "../../store";
import {makeRequestError} from "../Error/requestError"

/**
 * формирование тела для запроса
 * @param data - объект с паролем и логином
 * @returns {FormData}
 */
let makeFormData = (data) => {
  let body = new FormData();
  body.append('username', data.username);
  body.append('password', data.password);
  return body;
}

/**
 * преобразование ответа в JSON, далее получение их него токена
 * @param response - ответ(строка)
 * @returns {{token: *}}
 */
let parseToken = (response) => ({
  token: JSON.parse(response).data.id
})

/**
 * функция получение токена по запросу
 * @param data - объект с паролем и логином
 * @returns {Promise<Error or string>}
 */
export function getToken(data) {
  return new Promise(function (resolve, reject) {
    let req = new XMLHttpRequest();
    req.open(
      'POST',
      store.state.baseUrl + store.state.logIn,
      true
    );
    req.send(makeFormData(data));

    req.onload = function () {
      if (this.status === 200)
        resolve(parseToken(this.response).token);
      else reject(makeRequestError(this));
    };

    req.onerror = function () {
      reject(new Error("Network Error"));
    };

  });
}
