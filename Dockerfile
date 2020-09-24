from rpy2/jupyter

ENV NB_USER jupyteruser

USER root

RUN chown -R "${NB_USER}" /usr/local/lib/R/site-library

USER $NB_USER

