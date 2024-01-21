import api from ".";

const baseUrl = "/start";

export const _fetch_estados = async (params) => {
  return api
    .get(`${baseUrl}/federativas`)
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

export const _fetch_cidades = async (estado) => {
  return api
    .get(`${baseUrl}/municipios/${estado}`)
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

export const _fetch_escolas = async (params) => {
  return api
    .get(`${baseUrl}/filter${params}`)
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