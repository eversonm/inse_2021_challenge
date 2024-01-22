import api from ".";

const baseUrl = "/start";

export const _fetch_piores_escolas = async () => {
  return api
    .get(`${baseUrl}/escola/piores`)
    .then((response) => {
      if (response?.status === 200) {
        return response.data;
      }
      return response;
    })
    .catch((error) => {
      throw new Error(String(error));
    });
};
