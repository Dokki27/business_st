# 텍스트
### 일반 텍스트트

import streamlit as st

st.write('# 마크다운 H1 : st.write()')
st.write('## 마크다운 H2 : st.write()')
st.write('### 마크다운 H3 : st.write()')
st.write('')

st. title('제목 : st.title()')
st.header('헤더 : st.header()')
st.subheader('서브헤더 : st.subheader()')
st.text('본문 텍스트 : st.text()')
st.write('')

st.markdown('## 마크다운: st.markdown()')
st.markdown(
    '''
    # 마크다운 헤더1
    - 마크다운 목록1. **굵게** 표시
    - 마크다운 목록2.  *기울임* 표시
        -마크다운 목록2-1
        -마크다운 목록2-2

    ## 마크다운 헤더2
    - [네이버](https://naver.com)
    - [구글](https://google.com)

    ### 마크다운 헤더3
    일반 텍스트
    '''
)

st.divider()

st.caption('캡션(작고 흐린 글씨로 표현됨) : st.caption()')

st.write('##### 코드 블록: st.code()')
st.code('print("Hello, World!")', language='python')
st.code('print("Hello, World!")', language='python')
st.code('print("Hello, World!")', language='python', line_numbers=True)

st.write('##### 코드 블록: Markdown')
st.write(
    '''
    ```python
    print("Hello, World!")
    ```
    '''

)

st.write('##### 코드+결과: st.echo()')
with st.echo():
        name = 'Chunghun Ha'
        st.write("Hello, Streamlit!", name)

st.write('##### Latex 수식 작성: st.latex()')
st.latex('\int_a^b f(x)dx')

st.write('##### Latex 수식 작성: Markdown')
st.write('$$\int_a^b f(x)dx$$')

'''### 👑 Magic 적용
1. ordered item
    - 강조: **unordered item**
    - 기울임: *unordered item*
2. ordered item
3. ordered item
'''

'''#### 텍스트 색상 변경
- :red[빨간색 텍스트]
- :blue[파란색 텍스트]
- :green[초록색 텍스트]
- :orange[주황색 텍스트]
- :gray[회색 텍스트]
'''



'# 📚: 콜아웃'

'#### :orange[정보: st.info()]'
st.info('This is a purely informational message', icon= "ℹ️")

'#### :orange[경고: st.warning()]'
st.warning('This is a warning message', icon="⚠️")
st.title('첫번째 웹 어플 만들기🔥🫶')
st.title('두번째 웹 어플 만들기🔥🫶')
st.title('세번째 웹 어플 만들기🔥🫶')
st.write('#1. Markdown 텍스트 작성하기')
st.markdown(
    '''
    # 마크다운 헤더1
    - 마크다운 목록1. **굵게** 표시
    - 마크다운 목록2.  *기울임* 표시
    '''
)

st.image("bpbp.png", caption="부리부리대마왕", width=500)
