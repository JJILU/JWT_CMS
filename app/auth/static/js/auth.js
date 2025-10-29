alert("connected!!")

document.addEventListener("DOMContentLoaded", () => {

  const API_BASE = '/'
  
  registerForm = document.getElementById('registrationForm')
  loginForm = document.getElementById('loginForm')
  loginMsg = document.getElementById('loginMsg')

  if (registerForm) {
    // ======= Registration Form ===========
     registerForm.addEventListener("submit", async (e) => {
      e.preventDefault()

     teacher_id = document.getElementById('teacher_id').value.trim()
     password = document.getElementById('password').value.trim()


     console.log(teacher_id,password)



     if (!teacher_id || !password) {
      loginMsg.innerText = "teacher id and password are required fields!!"
      return
     }

     const res = await fetch(`/register`, {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({teacher_id,password})
     })


     const data = await res.json()


     if (res.status === 201) {
      registerForm.style.color = "green"
      registerForm.innerText =  data.message || "Registration Successfull!"
      setTimeout(() => {
        window.location.href = "/auth/"
      }, 1000)
     } 
     else
     {
      registerForm.style.color = "red"
      registerForm.innerText =  data.error || "Registration Failed!!"
      setTimeout(() => {
        window.location.href = "/auth/register"
      }, 1000)
     }
     })

  }
  else {
    // ======= Login Form ===========
    loginForm.addEventListener("submit", async (e) => {
      e.preventDefault()

     teacher_id = document.getElementById('teacher_id').value.trim()
     password = document.getElementById('password').value.trim()

     console.log(teacher_id,password)


     if (!teacher_id || !password) {
      errorMsg.innerText = "teacher id and password are required fields!!"
      return
     }

     const res = await fetch(`${API_BASE}`, {
      method: "POST",
      headers: {"Content-Type":"application/json"},
      body: JSON.stringify({teacher_id,password})
     })


     const data = await res.json()


     if (res.status === 200) {
      loginMsg.style.color = "green"
      loginMsg.innerText = data.message || "Login Successfull!"
      setTimeout(() => {
        window.location.href = "/dash/"
      },1000)
     }
     else {
      loginMsg.style.color = "red"
      loginMsg.innerText = data.error || "Login Failed!"
      setTimeout(() => {
        window.location.href = "/"
      },1000)
     }
     })

  }

})