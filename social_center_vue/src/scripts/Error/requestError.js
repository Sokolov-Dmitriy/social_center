/**
 * создание ошибки в случае неверного запроса
 * @param obj - объект ответа
 * @returns {Error}
 */
export let makeRequestError = (obj) => {
  let error = new Error(obj.statusText);
  error.code = obj.status;
  return error;
}
